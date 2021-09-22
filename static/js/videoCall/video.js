var websocket;


var yourVideo = document.getElementById("yours");
var theirVideo = document.getElementById("theirs");
var Connection;


function startPeerConnection() {
    //return;
    var config = {
        'iceServers': [
            //{ 'urls': 'stun:stun.xten.com:3478' },
            //{ 'urls': 'stun:stun.voxgratia.org:3478' },
            { 'url': 'stun:stun.l.google.com:19302' }
        ]
    };
    config = {
        iceServers: [
            { urls: 'stun:stun.l.google.com:19302' },
            { urls: 'stun:global.stun.twilio.com:3478?transport=udp' }
        ],
        //sdpSemantics: 'unified-plan'
    };
    // {
    //     "iceServers": [{
    //         "url": "stun:stun.1.google.com:19302"
    //     }]
    // };
    Connection = new RTCPeerConnection(config);
    Connection.onicecandidate = function(e) {
        console.log('onicecandidate');
        if (e.candidate) {
            websocket.send(JSON.stringify({
                "userid":userid,
                "event": "_ice_candidate",
                "data": {
                    "candidate": e.candidate
                }
            }));
        }
    }
    Connection.onaddstream = function(e) {
        console.log('onaddstream');

        //theirVideo.src = window.URL.createObjectURL(e.stream);
        theirVideo.srcObject = e.stream;
    }
}


createSocket();
startPeerConnection();

function f() {
    navigator.getUserMedia({ video: true, audio: true },
        stream => {
            yourVideo.srcObject = stream;
            window.stream = stream;
            Connection.addStream(stream)
        },
        err => {
            console.log(err);
        })
}


function createOffer(){
    //发送offer和answer的函数，发送本地session描述
    Connection.createOffer().then(offer => {
        Connection.setLocalDescription(offer);
        websocket.send(JSON.stringify({
            "userid":userid,
            "event": "offer",
            "data": {
                "sdp": offer
            }
        }));
    });
}



function createSocket(){
    var user = Math.round(Math.random()*1000) + ""
    websocket = new WebSocket("ws://127.0.0.1:8080/msgServer/"+user);
    eventBind();
};
function eventBind() {
    //连接成功
    websocket.onopen = function(e) {
        console.log('连接成功')
    };
    //server端请求关闭
    websocket.onclose = function(e) {
        console.log('close')
    };
    //error
    websocket.onerror = function(e) {

    };
    //收到消息
    websocket.onmessage = (event)=> {
    var json = JSON.parse(event.data);
        if(json.userid !=userid){
            //如果是一个ICE的候选，则将其加入到PeerConnection中，否则设定对方的session描述为传递过来的描述
            if(json.event === "_ice_candidate"&&json.data.candidate) {
                Connection.addIceCandidate(new RTCIceCandidate(json.data.candidate));
            }
            else if(json.event ==='offer'){
                Connection.setRemoteDescription(json.data.sdp);
                Connection.createAnswer().then(answer => {
                    Connection.setLocalDescription(answer);
                    console.log(window.stream);
                    websocket.send(JSON.stringify({
                        "userid":userid,
                        "event": "answer",
                        "data": {
                            "sdp": answer
                        }
                    }));
                })
            }
            else if(json.event ==='answer'){
                Connection.setRemoteDescription(json.data.sdp);
                console.log(window.stream)
            }
        }

    };
}
