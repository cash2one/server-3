/**
 * Created by sugar on 16/4/1.
 */
function preImg() {
                if (typeof FileReader === 'undefined') {
                    alert('Your browser does not support FileReader...');
                    return;
                }
                var reader = new FileReader();

                reader.onload = function(e) {
                    var img = document.getElementById("avator_logo");
                    img.src = this.result;
                }
                reader.readAsDataURL(document.getElementById("fileinput").files[0]);
            }

            function readFileInfo(source){
                var file = document.getElementById(source).files[0];
                if(file){
                    var size = 0;
                    if(file.size > 1024*1024){
                         fileSize = (Math.round(file.size * 100 / (1024 * 1024)) / 100).toString() + 'MB';
                    }
                    else{
                         fileSize = (Math.round(file.size * 100 / 1024) / 100).toString() + 'KB';
                    }
                    var name = file.name;

                    var type = file.type;
                }


            }