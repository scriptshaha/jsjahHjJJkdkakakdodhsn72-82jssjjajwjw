# Basic websocket port on 8766

import asyncio
import websockets

async def handle_client(websocket):
    print(f"Client connected from {websocket.remote_address}")
    
    try:
        async for message in websocket:
            print(f"Received: {message}")
            await websocket.send(f"Echo: {message}")
    except websockets.exceptions.ConnectionClosed:
        print(f"Client disconnected from {websocket.remote_address}")

async def main():
    print("Starting WebSocket server on ws://0.0.0.0:8766")
    
    async with websockets.serve(handle_client, "0.0.0.0", 8766):
        print("Server is running. Press Ctrl+C to stop.")
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer stopped.")
