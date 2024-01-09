// cpmoore0317

export default function getStudentsIdsSum(students) {
  const sumIds = students.reduce((sum, students) => sum + students.id, 0);
  return sumIds;
}
