import axios from "axios";
const { REACT_APP_ENDPOINT_API } = process.env;

const headers = {
  Authorization: "Basic " + btoa("admin.test11@gmail.com:Dcba654321"),
};

export const GetUserInfo = async (id) => {
  const URL = `${REACT_APP_ENDPOINT_API}employee/${id}/`;
  return await axios.get(URL, { headers });
};
