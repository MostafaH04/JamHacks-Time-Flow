
const auth = firebase.auth();

const whenSignedIn = document.getElementById('whenSignedIn');
const whenSignedOut = document.getElementById('whenSignedOut');

const signInBtn = document.getElementById('signInBtn');
const signOutBtn = document.getElementById('signOutBtn');

const userDetails = document.getElementById('userDetails');

const provider = new firebase.auth.GoogleAuthProvider();

signInBtn.onclick = () => auth.signInWithPopup(provider);
signOutBtn.onclick = () => auth.signOut();

auth.onAuthStateChanged(user =>{

    if (user){
        //when user is signed in, this should be maintained
        whenSignedIn.hidden = false;
        whenSignedOut.hidden= true;
        console.log({userDetails})

        let btn = document.createElement("button");
        btn.innerHTML = "Points";
        btn.type = "button";
        btn.name = "formBtn";
        document.body.appendChild(btn);

        function color(){
            document.getElementById('formBtn').style.backgroundColor='Aqua';
            setTimeout("ChangeColor1()",2000);
        }
    }
        else{

        whenSignedIn.hidden = true;
        whenSignedOut.hidden = false;
        formBtn.hidden = true;
        }



        }


);
