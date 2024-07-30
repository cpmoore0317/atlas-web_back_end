// 9-try.js

export default function guardrail(mathFuction) {
  const queue = [];

  try {
    const result = mathFuction();
    queue.push(result);
  } catch (error) {
    queue.push(error.toString());
  } finally {
    queue.push('Guardrail was processed');
  }

  return queue;
}
