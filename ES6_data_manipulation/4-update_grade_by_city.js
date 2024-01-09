// cpmoore0317

export default function updateStudentGradeByCity(students, city, newGrades) {
  const studentsInCity = students.filter(
    (student) => students.location === city
  );
  const updatedStudents = studentsInCity.map((student) => {
    const matchingGrade = newGrades.find(
      (grade) => grade.studentId === student.id
    );
    const updatedGrade = matchingGrade ? matchingGrade.grade : "N/A";
    return {
      id: student.id,
      firstName: student.firstName,
      location: student.city,
      grade: updatedGrade,
    };
  });
  return updatedStudents;
}
