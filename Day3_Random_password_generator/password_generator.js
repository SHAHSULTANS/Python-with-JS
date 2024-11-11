
const { promises } = require("dns");
const { resolve } = require("path");
const readline=require("readline")

const r1=readline.createInterface({
    input:process.stdin,
    output:process.stdout
});









function generatePassword(length = 8, useUppercase = true, useLowercase = true, useNumber = true, useSpecial = true) {
    let characterPool = "";

    if (useUppercase) characterPool += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if (useLowercase) characterPool += "abcdefghijklmnopqrstuvwxyz";
    if (useNumber) characterPool += "0123456789";
    if (useSpecial) characterPool += "!@#$%^&*()_+~`|}{[]\\:;?><,./-=";


    if(!characterPool){
        throw new Error("At least one character must be selected");
    }
    
    passwrod="";
    for(let i=0;i<length;i++){
        passwrod+=characterPool.charAt(Math.floor(Math.random()*characterPool.length));
    }

    return passwrod;
}

function askQuestion(query){
    return new Promise((resolve)=>r1.question(query,resolve));
}

async function mian() {

    console.log("Welcome to the Password Generator");
    
    const length=parseInt(await askQuestion("Enter the desired length of the password: "),10);
    // console.log(length);

    const uppercase=(await askQuestion("Include uppercase letters? (y/n): ")).trim().toLowerCase()==='y';

    const lowercase = (await askQuestion("Include lowercase letters? (y/n): ")).trim().toLowerCase() === 'y';
    const numbers = (await askQuestion("Include numbers? (y/n): ")).trim().toLowerCase() === 'y';
    const specialChar = (await askQuestion("Include special characters? (y/n): ")).trim().toLowerCase() === 'y';



    try{
       const ans= generatePassword(length,uppercase,lowercase,numbers,specialChar);
       console.log(ans)

    }
    catch(e){
        console.log(`${e}`);
    }
    r1.close();

}


mian()

