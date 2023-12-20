import axios from "axios";
import config from "./config";

// instance.interceptors.request.use(
//   (config) => {
//     config.headers.Authorization = `Bearer ${localStorage.getItem("token")}`;
//     return config;
//   }
// )



// TODO: figure out a sane way to add interceptors
//       and error handling

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
      return response.statusText === 'OK';
    })
    .catch(error => {
      console.log(error.message);
      return false;
    });
}

export async function getUsersReports() {
  client.interceptors.request.use(
    (config) => {
      config.headers.Authorization = `Bearer ${localStorage.getItem("token")}`;
      return config;
    }
  );
  return await client.get("reports/me")
    .then(response => { return response.data; })
    .catch(error => {
      alert(error.message);
    })
}

export async function generateReport(suspectName, websiteName) {
  client.interceptors.request.use(
    (config) => {
      config.headers.Authorization = `Bearer ${localStorage.getItem("token")}`;
      return config;
    }
  );

  await client.post(`reports/${websiteName}`, null, { params: {
    username: suspectName
  }
  })
    .then(response => {})
    .catch(error => {
      alert(error.message);
    });
}



