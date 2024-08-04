using System.Windows.Forms;
using System.Data.SqlClient;
using System.Data;
using System.Configuration;

namespace Lab2
{
    public partial class Form1 : Form
    {

        SqlConnection conn;
        SqlDataAdapter daBranch;
        SqlDataAdapter daEmployee;
        DataSet dset;
        BindingSource bsBranch;
        BindingSource bsEmployee;

        SqlCommandBuilder cmdBuilder;

        string queryBranch;
        string queryEmployee;
        string parentTable;
        string childTable;
        string foreignKey;

        public Form1()
        {
            InitializeComponent();
            FillData();
        }

        void FillData()
        {
            parentTable = ConfigurationManager.AppSettings["parentTable"];
            childTable = ConfigurationManager.AppSettings["childTable"];
            foreignKey = ConfigurationManager.AppSettings["foreignKey"];
            conn = new SqlConnection(getConnectionString());

            queryBranch = "SELECT * FROM " + parentTable;
            queryEmployee = "SELECT * FROM " + childTable;

            daBranch = new SqlDataAdapter(queryBranch, conn);
            daEmployee = new SqlDataAdapter(queryEmployee, conn);
            dset = new DataSet();
            daBranch.Fill(dset, parentTable);
            daEmployee.Fill(dset, childTable);

            cmdBuilder = new SqlCommandBuilder(daEmployee);

            dset.Relations.Add("BranchEmployee",
                dset.Tables[parentTable].Columns[foreignKey],
                dset.Tables[childTable].Columns[foreignKey]);

            this.dataGridView1.DataSource = dset.Tables[parentTable];
            this.dataGridView2.DataSource = this.dataGridView1.DataSource;
            this.dataGridView2.DataMember = "BranchEmployee";

            cmdBuilder.GetUpdateCommand();
        }

        string getConnectionString()
        {
            return "Data Source=DESKTOP-KQB7ODH;" + "Initial Catalog=Sales Management;Integrated Security=true;";

        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                daEmployee.Update(dset, childTable);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Exception " + ex.Message, "Error");
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            foreach (DataGridViewRow row in dataGridView2.SelectedRows)
            {
                if (!row.IsNewRow)
                {
                    DataRowView drv = (DataRowView)row.DataBoundItem;
                    DataRow employeeRow = drv.Row;
                    employeeRow.Delete();
                    daEmployee.Update(dset, childTable);
                }
            }
        }
    }
}