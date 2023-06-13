<template>
  <div>
    <p>{{ msg }}</p>
  </div>
  <div>
    <button @click="sendPostRequest">POST 요청 보내기</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PingComponent',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      axios.get('/')
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    sendPostRequest() {
      const data = {
        // title: '제목',
        // content: '내용'
      };
      console.log("click event")
      axios.post('http://localhost:8000/todo', data)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};

</script>
