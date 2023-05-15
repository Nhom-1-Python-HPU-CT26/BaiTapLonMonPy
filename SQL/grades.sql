select student.name, grade.*
from student
inner join grade on grade.studentid = student.studentid;