// 3-get_ids_sum.js

export default function getStudentsIdsSum(students) {
  const sumIds = students.reduce((sum, students) => sum + students.id, 0);
  return sumIds;
}
