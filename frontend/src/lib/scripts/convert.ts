/**
 * 
 * @param inputString - "1234567890"
 * @returns 
 */
export function convertStringToMatrix(inputString: string): number[][] {
  const matrix: number[][] = [];
  
  const row: number[] = [];
  [...inputString].forEach((element: string, index: number) => {
    row.push(parseInt(element));
    if ((index) % 3 == 2) {
      matrix.push([...row]);
      row.splice(0, row.length)
    }
  });

  return matrix;
}