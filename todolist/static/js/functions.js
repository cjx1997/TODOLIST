dopost=function(id,st) {
            var postform = document.createElement("form");
            postform.method="post";
            postform.action="/business/solve";
            idinput = document.createElement("input");
            idinput.setAttribute("name","id");
            idinput.setAttribute("value",id);
            postform.appendChild(idinput);
            tokeninput = document.createElement("input");
            tokeninput.setAttribute("name","csrfmiddlewaretoken");
            tokeninput.setAttribute("value",st.slice(55,87));
            postform.appendChild(tokeninput);
            document.body.appendChild(postform);
            postform.submit();
            document.body.removeChild(postform);
        }
dodelete=function(id,st) {
            var postform = document.createElement("form");
            postform.method="post";
            postform.action="/business/delete";
            idinput = document.createElement("input");
            idinput.setAttribute("name","id");
            idinput.setAttribute("value",id);
            postform.appendChild(idinput);
            tokeninput = document.createElement("input");
            tokeninput.setAttribute("name","csrfmiddlewaretoken");
            tokeninput.setAttribute("value",st.slice(55,87));
            postform.appendChild(tokeninput);
            document.body.appendChild(postform);
            postform.submit();
            document.body.removeChild(postform);
        }
save=function() {
            var text=document.getElementById("content");
            var postform = document.createElement("form");
            var id=getid();
            var st=csrf;
            postform.method="post";
            postform.action="/business/edit";
            idinput = document.createElement("input");
            idinput.setAttribute("name","id");
            idinput.setAttribute("value",id);
            postform.appendChild(idinput);
            tokeninput = document.createElement("input");
            tokeninput.setAttribute("name","csrfmiddlewaretoken");
            tokeninput.setAttribute("value",st.slice(55,87));
            contentinput = document.createElement("input");
            contentinput.setAttribute("name","content");
            contentinput.setAttribute("value",text.value);
            postform.appendChild(tokeninput);
            postform.appendChild(contentinput);
            document.body.appendChild(postform);
            postform.submit();
            document.body.removeChild(postform);
}
edit=function() {
            var text=document.getElementById("content");
            var butt=document.getElementById("edit");
            butt.innerText="Save";
            butt.setAttribute("class","btn btn-default btn-success");
            butt.onclick=save;
            text.removeAttribute("disabled");
}