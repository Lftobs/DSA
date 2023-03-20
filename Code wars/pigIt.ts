export const pigIt = (a : string) : string =>  {
  let edited: string[] =[]
  let wordsArray : string[] = a.split(" ")
  wordsArray.forEach( (word) => {
      let charArray: string[] = word.split('')
      let char: string = charArray[0]
    
      if (/[~`!@#$%^&*(){}\[\];:"'<,.>?\/\\|_+=-]/.test(char) == false) {
          charArray.shift()
          charArray.push(`${char}ay`)
      }    

      let str: string = charArray.join('')

      if (str == 'undefineday') {
          edited.push('')
      } else {
          edited.push(str)
      }    

  }) 

  return edited.join(' ')

}
