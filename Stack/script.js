function pushitem() {
    var item = document.querySelector('.pusheditem').value;

    var tr= document.createElement('tr');

    var td1=tr.appendChild(document.createElement('td'));
    
    td1.innerhtml = item;
    document.getElementById('main').appendChild(tr);
}


// document.querySelector('.main').innerHTML = <ul>${display(array)}</ul>;
// let pushbtn = document.querySelector('.pushbtn');
// pushbtn.addEventListener('click', pushitem);