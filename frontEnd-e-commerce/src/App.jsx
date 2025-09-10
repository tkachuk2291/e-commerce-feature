import {BrowserRouter, Route, Routes} from "react-router-dom";
import ProductList from "./components/ProductList/ProductList.jsx";
import ProductDetails from "./components/ProductDetails/ProductDetails.jsx";

function App() {


    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route path="/products" element={<ProductList/>}/>
                    <Route path="/products/:productId" element={<ProductDetails/>}/>

                </Routes>

            </BrowserRouter>

        </>
    )
}

export default App
