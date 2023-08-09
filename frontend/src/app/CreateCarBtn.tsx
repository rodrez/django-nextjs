"use client";
export default function CreateCarBtn() {
  const createCar = async () => {
    const res = await fetch("http://127.0.0.1:8000/api/create-car/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: "Ford",
        color: "red",
        price: 1000,
      }),
    });
    const data = await res.json();
    console.log(data);
  };
  return (
    <div>
      <button className="bg-blue-400 p-2 rounded-md" onClick={createCar}>
        Create Car
      </button>
    </div>
  );
}
