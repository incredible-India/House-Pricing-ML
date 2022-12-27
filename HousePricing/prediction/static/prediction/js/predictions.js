var btn = document.getElementById('estimateprice')
var bhk = document.getElementById('bhk')
var bath = document.getElementById('bath')
var location = document.getElementById('location')
var sqft = document.getElementById('sqft')

console.log('hello world');

btn.addEventListener('click', ()=>{

    let xhr = new XMLHttpRequest();

    xhr.open('POST',`${location.href}`,true);


    xhr.onprogress = ()=>{
        document.getElementsByClassName('loading')[0].style.display = 'block';

    }

    xhr.onload = ()=>{

        document.getElementsByClassName('loading')[0].style.display = 'none';
    }

})