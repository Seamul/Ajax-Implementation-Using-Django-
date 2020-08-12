// alert("sdnnj");
window.onload=initAll;
var saveBookButton;
var showbook
function initAll(){

	saveBookButton= document.getElementById('save_book');
	saveBookButton.onclick=savebook;

	
}
function savebook()
{
	var name=document.getElementById("book_name").value;
	var prize=document.getElementById("book_prize").value;
	var pages=document.getElementById("book_pages").value;
	var url ='/save_book?name='+name+'&prize='+prize+'&pages='+pages;
	
	  var req= new XMLHttpRequest();
  req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    	
    	     if(req.responseText)
    	     {
    	     	alert("SAVE YOUR ITEMS");
    	     	document.getElementById("book_name").value='';
	            document.getElementById("book_prize").value='';
	            document.getElementById("book_pages").value='';
    	     }
     
    }
  };
  req.open("GET", url, true);
  req.send();
}
function showAllBook()
{
	 var req= new XMLHttpRequest();
	 var url='/getAllBook'
     req.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) {
     	 // req.responseText dara request gulo ase
    	//eval dara json string k json object a convert kora hoy
	     var data=eval(req.responseText)
	     var div=document.getElementById('profile');
	     // bar bar click korle akoi table jate bar bar na ase se jnno empty string bebohar kora hoy
	     div.innerHTML="";
     var table=document.createElement('TABLE');
     // 0 index ar row toi kore tar por innerHtml dara name parize ar pages insert kora hoiche
     var row=table.insertRow(0);
     var name=row.insertCell(0);
     var prize=row.insertCell(1);
     var pages=row.insertCell(2);
     var clicktodilit=row.insertCell(3)
     name.innerHTML="Book name";
     prize.innerHTML="Prize";
     pages.innerHTML="Pages";
     clicktodilit.innerHTML="Click to  Delete";
     clicktodilit.className="text-danger text-center"

     for(i=0;i<data.length;i++)
     {
     	var row=table.insertRow(i+1);
     	var name=row.insertCell(0);
     	var prize=row.insertCell(1);
     	var pages=row.insertCell(2);
     	var clicktodilit=row.insertCell(3);
     	name.innerHTML=data[i].name;
     	prize.innerHTML=data[i].prize;
     	pages.innerHTML=data[i].pages;
     	// for delete icon &times
     	clicktodilit.innerHTML="&times";
     	//bootstrap for delete icon
     	clicktodilit.className="text-danger text-center"
     	clicktodilit.style.fontSize="25px";
     	clicktodilit.style.cursor="pointer";
     	clicktodilit.className="deletebutton";
     	//finding id for delete item
     	clicktodilit.id=data[i].id;
     	clicktodilit.onclick=function()
     	{
     		var obj= this;
     		var id =this.id;
     		var url='/deletebook?id='+id;
     		var req= new XMLHttpRequest();
            req.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
            	
            	if(req.responseText=='true')
            	{
            		// alert(req.responseText)
            		table.deleteRow(obj.parentNode.rowIndex);
            	}
     
    }
  };
  req.open("GET", url, true);
  req.send();

     	}
 

     }
     // bootstrep table ar jonno
     table.className='table text-center';
     div.appendChild(table)

    }
  };
  req.open("GET", url, true);
  req.send();
 }
