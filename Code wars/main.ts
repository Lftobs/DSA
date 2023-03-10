function toCamelCase(str:string) : string {
         for (let i=0; i < str.length; i++) {
             if (str[i]=='-' || str[i]=='_' || str[i]==' ') {
                let y: string  = str[i + 1].toUpperCase()
                str = str.substring(0, i+1) + y + str.substring(i+1 + y.length)
                str = str.replace(str[i], '')
             }
         }
         return str
}
