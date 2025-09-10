export async function  get(url){
    const baseUrl = import.meta.env.VITE_API_URL
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const myRequest = new Request("https://e-commerce-feature.onrender.com/" + url , {
        method: "GET",
        headers: myHeaders,
    });
    return  await  fetch(myRequest)
}

