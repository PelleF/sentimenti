
export async function MakeCall(companyName) {

    try{
        // Set the company name as query parameter
        const encodedValue = encodeURIComponent(companyName);
        const response = await fetch(`http://127.0.0.1:8000/polls/?companyName=${encodedValue}`);

        return await response.json();
    }catch(error) {
        return [];
     }
}
