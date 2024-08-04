using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.Data.SqlClient;

namespace Lab1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string constring = "Data Source=DESKTOP-KQB7ODH;" + "Initial Catalog=Sales Management;Integrated Security=true;";

            SqlConnection con = new SqlConnection(constring);

            con.Open();

            string strSalesManagement = "SELECT * FROM branch";
            SqlCommand cmd = new SqlCommand(strSalesManagement, con);
            using(SqlDataReader reader = cmd.ExecuteReader())
            {
                while (reader.Read())
                {
                    Console.WriteLine("{0}, {1}", reader[0], reader[1]);
                }
            }

            SqlDataAdapter sqlDataAdapter = new SqlDataAdapter(strSalesManagement, con);
            DataSet set = new DataSet();

            sqlDataAdapter.Fill(set, "branch");
            foreach(DataRow pRow in set.Tables["branch"].Rows)
            {
                Console.WriteLine("{0} {1}", pRow["branch_id"], pRow["branch_name"]);
            }

            con.Close();
        }
    }
}
