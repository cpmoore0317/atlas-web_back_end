// cpmoore0317

export default function getStudentsByLocation(students, city) {
  const locationBasedList = students.filter(
    (student) => student.location === city
  );
  return locationBasedList;
}
