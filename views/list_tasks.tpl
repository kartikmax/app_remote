<head>
  <link
    href="https://cdn.jsdelivr.net/bootstrap/3.3.6/css/bootstrap.min.css"
    rel="stylesheet"
  />
</head>
<body>
  <ol>
  % for task in list:
  <li>
    <a
      href="https://app.asana.com/0/{{proj_id}}/{{task['gid']}}"
      target="_blank"
      >{{task['name']}}</a
    >
  </li>
  % end
</ol>
<script src="https://static.zdassets.com/zendesk_app_framework_sdk/2.0/zaf_sdk.min.js"></script>
<script>
  const action = "notifySuccess"
</script>
<script src="js/main.js"></script>
</body>