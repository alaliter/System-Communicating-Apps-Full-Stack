class fetchRequestPackage {
    constructor(height, width) {
        this.common_url = 'http://tinman.cs.gsu.edu:5001/';
        this.token = '';
    }

    fetchRequest(url, method, params = ''){
        let header = {
            "Content-Type": "application/json;charset=UTF-8",
            "accesstoken":this.token  
        };
        console.log('request url:', url, params);  
        let that = this;
        if(params == ''){   
            return new Promise(function (resolve, reject) {
                fetch(that.common_url + url, {
                    method: method,
                    headers: header
                }).then(
                    (response) => {
                        console.log("");
                        return response.json()
                    })
                    .then((responseData) => {
                        console.log('res:',url,responseData);  
                        resolve(responseData);
                    })
                    .catch( (err) => {
                        console.error('err:',url, err);     
                        reject(err);
                    });
            });
         }else{   
            return new Promise(function (resolve, reject) {
                fetch(that.common_url + url, {
                    method: method,
                    headers: header,
                    body: params   
                })
                .then((response) => response.json())
                .then((responseData) => {
                    // var parsedData = JSON.parse(responseData);
                    // console.log('res:',url, responseData);   
                    resolve(responseData);
                })
                .catch( (err) => {
                    console.error('err:',url, err);   
                    reject(err);
                });
            });
        }
    }
}

export default fetchRequestPackage;
