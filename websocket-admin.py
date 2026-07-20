class ConnectionManager():
  def __init__(self):
    self.connections = {}
    def connect(self, token):
      await websocket.accept()
      self.connections[websocket] = token
      print(f"Client connected. Total: {len(connected_clients)}")
      try:
        while True:
            data = await websocket.receive_json()
            print(f"Received: {data}")

        
            try:
               await main(data)
            except Exception as e:
               print("Processing error:", e)
               await websocket.send_json({"message": "error", "error": str(e)})


    except WebSocketDisconnect:
        
    def disconnect(websocket):
      connected_clients.pop(websocket, None)
      print(f"Client disconnected. Total: {len(connected_clients)}")
    def 
      
