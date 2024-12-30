const leftmenu=document.querySelector('.left-menu');
const tgbtn=document.createElement('button');
const maincontent=document.createElement('main-content');



tgbtn.textContent='Toggle-Button';
tgbtn.classList.add('toggle-button');

tgbtn.addEventListener('click',()=>{
    if(leftmenu.style.display==='none'|| leftmenu.style.display === ''){
        leftmenu.style.display='block';
    }else{
        leftmenu.style.display='none';
    }
});
document.body.appendChild(tgbtn);
function adwidth(){
    const width=window.innerWidth;
    document.body.classList.remove('shrink-90','shrink-80','shrink-75','shrink-50');
    if(width<=600){
        maincontent.classList.add('shrink-50');
    }
    else if(width>600 && width<=700){
        maincontent.classList.add('shrink-75');
    }else if(width>700 && width<=767){
        maincontent.classList.add('shrink-80');
    }else if(width>992 && width<=1600){
        maincontent.classList.add('shrink-90');
    }
}
window.addEventListener('resize',adwidth);
document.addEventListener('DOMContentLoaded',adwidth);