using lab_9.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using lab_9.Data_Abstraction_Layer;
using static Org.BouncyCastle.Bcpg.Attr.ImageAttrib;

namespace lab_9.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            return View();
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [HttpGet("/student")]
        public IActionResult GetStudents([FromQuery] int group_id, [FromQuery] int page = 1)
        {
            DataAbstractionLayer dal = new DataAbstractionLayer();
            return Ok(dal.GetStudentsFromGroup(group_id, page));
        }

        [HttpGet("/teacher")]
        public IActionResult GetTeachers()
        {
            DataAbstractionLayer dal = new DataAbstractionLayer();
            return Ok(dal.GetTeachers());
        }

        [HttpGet("/grades")]
        public IActionResult GetGrades([FromQuery] int student_id)
        {
            DataAbstractionLayer dal = new DataAbstractionLayer();
            return Ok(dal.GetStudentGrades(student_id));
        }

        [HttpPost("/add_grade")]
        public IActionResult AddGrade([FromBody] FormData formData)
        {

            DataAbstractionLayer dal = new DataAbstractionLayer();
            dal.AddGrade(formData.student_id, formData.grade, formData.course);
            return Ok();
        }

        [HttpPost("/edit_grade")]
        public IActionResult EditGrade([FromBody] EditForm formData)
        {
            DataAbstractionLayer dal = new DataAbstractionLayer();
            dal.EditGrade(formData.grade_id ,formData.course, formData.grade );
            return Ok();
        }


        [HttpPost("/login")]
        public IActionResult Login([FromForm] string name, [FromForm] string password)
        {
            DataAbstractionLayer dal = new DataAbstractionLayer();
            List<Student> students = dal.GetStudents();
            List<Teacher> teachers = dal.GetTeachers();
            foreach (Student student in students)
            {
                if (student.name == name && student.password == password)
                {
                    return Ok(new { userType = "student", studentId = student.id });
                }
            }

            foreach (Teacher teacher in teachers)
            {
                if (teacher.name == name && teacher.password == password)
                {
                    return Ok(new { userType = "teacher"});
                }
            }

            return Unauthorized();
        }


        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
