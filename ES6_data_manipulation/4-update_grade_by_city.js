// 4-update_grade_by_city.js

export default function updateStudentGradeByCity(students, city, newGrades) {
  const studentsInCity = students.filter(
    (student) => students.location === city
  );
  const updatedStudents = studentsInCity.map((student) => {
    const matchingGrade = newGrades.find(
      (grade) => grade.studentId === student.id
    );
    return { ...student, grade: matchingGrade ? matchingGrade.grade : "N/A" };
  });
  return updatedStudents;
}
