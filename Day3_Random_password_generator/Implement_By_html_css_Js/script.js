function generatePassword() {
    //alert("YeS");
    const length = parseInt(document.getElementById("length").value);

    const upperChecked = document.getElementById("uppercase").checked;
    const lowerChecked = document.getElementById("lowercase").checked;
    const numberChecked = document.getElementById("numbers").checked;
    const specialChecked = document.getElementById("special").checked;
    //alert(upperChecked)

    let charPoll = "";


    if (upperChecked) charPoll += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if (lowerChecked) charPoll += "abcdefghijklmnopqrstuvwxyz";
    if (numberChecked) charPoll += "0123456789";
    if (specialChecked) charPoll += "!@#$%^&*()_+[]{}|;:,.<>?";

    if (!charPoll) {
        alert("Please select at least one character type.");
    }

    let password = "";
    for (let i = 0; i < length; i++) {
        password += charPoll[Math.floor(Math.random() * charPoll.length)];
    }

    document.getElementById("result").textContent = password;

}



function copyPassword() {
    const password = document.getElementById("result").textContent;
    navigator.clipboard.writeText(password)
        .then(() => {
            alert("Password copied to clipboard!");
        })
        .catch(err => {
            console.error('Failed to copy password: ', err);
        });
}