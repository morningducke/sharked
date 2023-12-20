import axios from "axios";
import config from "./config";

// instance.interceptors.request.use(
//   (config) => {
//     config.headers.Authorization = `Bearer ${localStorage.getItem("token")}`;
//     return config;
//   }
// )




const client = axios.create({
  baseURL: config.apiBasePath,
  withCredentials: true
});
  
export async function login(username, password) {
  return await client.post("users/login", {
    username: username,
    password: password
  }, {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
    .then(response => {
      localStorage['token'] = response.data['access_token'];
      client.interceptors.request.use(
        (config) => {
          config.headers.Authorization = `Bearer ${localStorage.getItem("token")}`;
          return config;
        }
      )
      return response.statusText === 'OK';
    })
    .catch(error => {
      console.log(error.message);
      return false;
    });
}



