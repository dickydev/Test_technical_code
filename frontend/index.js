// TEST API
function validateInput(){
    const input = document.getElementById('inputAngka').value;
    const errorMsg = document.getElementById('errorMsg');
    
    
    if(!/^\d+$/.test(input)){
        errorMsg.textContent = 'Masukkan angka yang valid';
        return false;
    }

    errorMsg.textContent = "";
    return true; 
    
}

function sendAjaxReq(endpoint){
    if(!validateInput()) return;

    const number = document.getElementById('inputAngka').value;

    fetch(endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({number: parseInt(number)})
    }).then(response => response.json()).then(data => {
        document.getElementById('result').innerText = data.result;
    }).catch((error)=>{
        console.error('Error:', error);
    })
}

function generateTriangle(){
    sendAjaxReq('http://127.0.0.1:8000/generate-triangle')
}

function generateOddNumber(){
    sendAjaxReq('http://127.0.0.1:8000/generate-odd-number')
}

function generatePrimeNumber(){
    sendAjaxReq('http://127.0.0.1:8000/generate-prime-number')
}