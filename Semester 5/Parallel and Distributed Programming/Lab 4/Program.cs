using System;
using System.IO;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

class HttpDownloader
{
    private Task ConnectAsync(Socket socket, string host, int port)
    {
        return Task.Factory.FromAsync(socket.BeginConnect, socket.EndConnect, host, port, null);
    }

    private Task<int> SendAsync(Socket socket, byte[] buffer)
    {
        var tcs = new TaskCompletionSource<int>();

        socket.BeginSend(buffer, 0, buffer.Length, SocketFlags.None, ar =>
        {
            try
            {
                int bytesSent = socket.EndSend(ar);
                tcs.SetResult(bytesSent);
            }
            catch (Exception ex)
            {
                tcs.SetException(ex);
            }
        }, null);

        return tcs.Task;
    }

    private Task<int> ReceiveAsync(Socket socket, byte[] buffer)
    {
        var tcs = new TaskCompletionSource<int>();

        socket.BeginReceive(buffer, 0, buffer.Length, SocketFlags.None, ar =>
        {
            try
            {
                int bytesReceived = socket.EndReceive(ar);
                tcs.SetResult(bytesReceived);
            }
            catch (Exception ex)
            {
                tcs.SetException(ex);
            }
        }, null);

        return tcs.Task;
    }

    public void DownloadFile(string host, string path, string outputFilePath)
    {
        var socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
        ConnectAsync(socket, host, 80).ContinueWith(connectTask =>
        {
            string request = $"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: Close\r\n\r\n";
            byte[] requestBytes = Encoding.ASCII.GetBytes(request);

            SendAsync(socket, requestBytes).ContinueWith(sendTask =>
            {
                byte[] buffer = new byte[8192];
                StringBuilder headers = new StringBuilder();
                bool headersParsed = false;
                using var fileStream = new FileStream(outputFilePath, FileMode.Create);

                void ReceiveLoop()
                {
                    ReceiveAsync(socket, buffer).ContinueWith(receiveTask =>
                    {

                        int received = receiveTask.Result;
                        if (received == 0)
                        {
                            fileStream.Close();
                            socket.Close();
                            Console.WriteLine($"File downloaded successfully to: {outputFilePath}");
                            return;
                        }

                        string responsePart = Encoding.ASCII.GetString(buffer, 0, received);

                        if (!headersParsed)
                        {
                            headers.Append(responsePart);
                            int headerEndIndex = headers.ToString().IndexOf("\r\n\r\n");
                            if (headerEndIndex >= 0)
                            {
                                headersParsed = true;
                                Console.WriteLine("Headers:\n" + headers.ToString(0, headerEndIndex) + "\n");

                                int bodyStartIndex = headerEndIndex + 4;
                                fileStream.Write(buffer, bodyStartIndex, received - bodyStartIndex);
                            }
                        }
                        else
                        {
                            fileStream.Write(buffer, 0, received);
                        }

                        ReceiveLoop();
                    });
                }

                ReceiveLoop();
            });
        });
    }
}

class Program
{
    static void Main(string[] args)
    {
        string host = "httpbin.org";
        string path = "/html";
        string outputFilePath = "downloaded_file_task.html";

        Console.WriteLine($"Downloading {path} from {host} using task-based approach with ContinueWith...");
        var downloader = new HttpDownloader();
        downloader.DownloadFile(host, path, outputFilePath);

        Console.ReadLine();
    }
}
