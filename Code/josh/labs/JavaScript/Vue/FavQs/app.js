let app = new Vue({
  el: "#app",
  data: {
    qotd: "",
    qotdAuthor: "",
    searchTerm: "",
    quotes: Array(),
  },
  mounted: () => {
    axios.get("https://favqs.com/api/qotd").then((response) => {
      app.qotd = response.data.quote.body;
      app.qotdAuthor = response.data.quote.author;
    });
  },
  methods: {
    getQuotes: () => {
      let url = "https://favqs.com/api/quotes/?filter=" + app.searchTerm;
      axios
        .get(url, {
          headers: { Authorization: "Token token=7335d37e253df30e09f8b550e8306148" },
        })
        .then((response) => {
          app.quotes = response.data.quotes;
        })
        .catch((err) => {
          console.log("error", err);
        });
    },
  },
});
