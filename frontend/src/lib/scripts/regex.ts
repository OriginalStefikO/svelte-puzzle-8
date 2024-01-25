export function checkInputString(inputString: string): boolean {  
  if (/^(?!.*(.).*\1)\d{9}$/.test(inputString)) {
    return true;
  }
  else if (inputString.length < 9) {
    return false
  }
  else if (inputString.length > 9) {
    return false
  }
  else {
    return false
  }
}