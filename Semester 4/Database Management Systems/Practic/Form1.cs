using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.Data.SqlClient;
using Microsoft.Data.SqlClient;

namespace Practic
{
    public partial class Form1 : Form
    {
        SqlConnection con;
        DataSet ds;
        SqlDataAdapter daModel, daProducer;
        SqlCommandBuilder cb;
        BindingSource bsModel, bsProducer;
        string constring = "Data Source=DESKTOP-KQB7ODH;Initial Catalog=Example;Integrated Security=True;TrustServerCertificate=True";

        public Form1()
        {
            InitializeComponent();

            con = new SqlConnection(constring);
            ds = new DataSet();
            daModel = new SqlDataAdapter("select * from Model", con);
            daProducer = new SqlDataAdapter("select * from Producer", con);
            cb = new SqlCommandBuilder(daModel);

            daModel.Fill(ds, "Model");
            daProducer.Fill(ds, "Producer");

            DataRelation dr = new DataRelation("FK_Model_Producer", ds.Tables["Producer"].Columns["pid"], ds.Tables["Model"].Columns["pid"]);
            ds.Relations.Add(dr);
            bsModel = new BindingSource();
            bsProducer = new BindingSource();

            bsProducer.DataSource = ds;
            bsProducer.DataMember = "Producer";

            bsModel.DataSource = bsProducer;
            bsModel.DataMember = "FK_Model_Producer";

            dataGridView1.DataSource = bsModel;
            dataGridView2.DataSource = bsProducer;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            daModel.Update(ds, "Model");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            foreach (DataGridViewRow row in dataGridView1.SelectedRows)
            {
                if (!row.IsNewRow)
                {
                    DataRowView drv = (DataRowView)row.DataBoundItem;
                    DataRow modelRow = drv.Row;
                    modelRow.Delete();
                    daModel.Update(ds, "Model");
                }
            }
        }
    }
}
