export default class PriceApi {

    public static async GetUser() {
        await fetch("http://localhost:8000/api/users")
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.log(error));
    }

    public static async GetCollection() {
        await fetch("http://localhost:8000/api/collections")
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.log(error));
    }
}