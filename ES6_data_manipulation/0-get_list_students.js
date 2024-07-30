// 0-get_list_students.js

export default function getListStudents() {
  const students = [];
  const guillaume = {
    id: 1,
    firstName: 'Guillaume',
    location: 'San Francisco',
  };
  const james = {
    id: 2,
    firstName: 'James',
    location: 'Columbia',
  };
  const serena = {
    id: 5,
    firstName: 'Serena',
    location: 'San Francisco',
  };
  students.push(guillaume, james, serena);
  return students;
}
