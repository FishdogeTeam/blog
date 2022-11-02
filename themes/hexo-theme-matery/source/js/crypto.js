// let getCryptoUrl =  "https://api2.fishdogeweb.store/getData?"
let getStockUrl = "https://api2.fishdogeweb.store/getStock?"
let getBlockHeightURL = "https://api2.fishdogeweb.store/getBlockHeight?"
// let apiErrMsg = "連不上API，請先連上API"

export async function getStock(){
    let data;
    let url = getStockUrl;
    // url need to be changed
    await axios.get(url)
    .then((response) => {
        data = response.data;
        // data = JSON.parse(JSON.stringify(response.data));
    })
    .catch((error) => {
        data = error;
        console.log(error);
    });
    return data;
}

export async function getBlockHeight(){
    let data;
    let url = getBlockHeightURL;
    // url need to be changed
    await axios.get(url)
    .then((response) => {
        data = response.data;
    })
    .catch((error) => {
        data = error;
        console.log(error);
    });
    return data;
}

export function setPriceGain(imgID, textID, gainID, data){
    if (data > 0){
        document.getElementById(imgID).classList.add("fa-caret-up");
        document.getElementById(imgID).classList.add("green-text");
        document.getElementById(textID).classList.add("green-text");
    } else if (data == 0){

    } else {
        document.getElementById(imgID).classList.add("fa-caret-down");
        document.getElementById(imgID).classList.add("red-text");
        document.getElementById(textID).classList.add("red-text");
        data *= -1;
    }
    document.getElementById(gainID).innerHTML = data + "%";
}