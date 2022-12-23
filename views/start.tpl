<head>
  <link
    href="https://cdn.jsdelivr.net/bootstrap/3.3.6/css/bootstrap.min.css"
    rel="stylesheet"
  />
</head>
<body>
  <a class="btn btn-default btn-block" href="list?{{qs}}" role="button"
    >List tech note ideas</a
  > 
  <a class="btn btn-default btn-block" href="list" role="button"
    >add tech note ideas</a
  >
  % if defined('error_msg'):
  <script src="https://static.zdassets.com/zendesk_app_framework_sdk/2.0/zaf_sdk.min.js"></script>
<script>
  const msg = "{{error_msg}}"
  const client = ZAFClient.init()
  client.invoke("notify", msg, "error")
</script>
% end
</body>
