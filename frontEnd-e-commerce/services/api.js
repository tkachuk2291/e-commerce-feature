export async function  get(url){
    const baseUrl = 'http://127.0.0.1:8000/'
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const myRequest = new Request(baseUrl + url , {
        method: "GET",
        headers: myHeaders,
    });
    return  await  fetch(myRequest)
}
