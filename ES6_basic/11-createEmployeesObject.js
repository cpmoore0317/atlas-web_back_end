// cpmoore0317

export default function createEmployeeObjects(departmentName, employees) {
  const departmentObject = {
    [departmentName]: employees,
  };

  return departmentObject;
}
