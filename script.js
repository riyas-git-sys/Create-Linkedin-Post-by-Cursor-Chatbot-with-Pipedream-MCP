function generatePost() {
  const text = document.getElementById('postText').value;
  const imageUrl = document.getElementById('imageUrl').value;
  console.log("MCP Prompt:", `Create post with text: "${text}" and image: ${imageUrl}`);
  alert("Check Cursor IDE's MCP tab to complete the request!");
}