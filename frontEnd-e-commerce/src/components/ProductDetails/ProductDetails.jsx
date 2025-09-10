import {Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow} from "@mui/material";
import {useEffect, useState} from "react";
import {get} from "../../../services/api.js";
import {Link, useNavigate, useParams} from "react-router-dom";
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import "./productDetails.scss"
import ImageIcon from '@mui/icons-material/Image';
import Box from "@mui/material/Box";


function ProductDetails() {

    const [product, setProduct] = useState(null)
    const {productId} = useParams();

    useEffect(() => {
        async function getProductList() {
            const response = await get(`products/${Number(productId)}`)
            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }
            const result = await response.json();

            setProduct(result)
        }

        getProductList()
    }, [productId]);

    const navigate = useNavigate();

    return (
        <>
            <div className={"main"}>
                <Box component="section" sx={{p: 2, border: '1px dashed grey' , textAlign: 'center'}}>
                    Product details
                </Box>
                <TableContainer component={Paper}>
                    <button onClick={() => navigate(-1)}   className={"button"}><ArrowBackIcon/></button>


                    <Table sx={{minWidth: 650}} aria-label="caption table">

                        <TableHead>
                            <TableRow>
                                <TableCell align='center'> name</TableCell>
                                <TableCell align="center"> description</TableCell>
                                <TableCell align="center"> price</TableCell>
                                <TableCell align="center"> stock</TableCell>
                                <TableCell align="center"> category</TableCell>
                                <TableCell align="center"> image</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {product && (
                                <TableRow key={product.id}>
                                    <TableCell align="center" component="th" scope="row">{product.name}</TableCell>
                                    <TableCell align="center">{product.description}</TableCell>
                                    <TableCell align="center">{product.price}</TableCell>
                                    <TableCell align="center">{product.stock}</TableCell>
                                    <TableCell align="center">{product.category}</TableCell>
                                    <TableCell align="center">
                                        <Link to={product.image} className={"link"}><ImageIcon /></Link>
                                    </TableCell>
                                </TableRow>
                            )}
                        </TableBody>
                    </Table>
                </TableContainer>
            </div>
        </>
    )
}

export default ProductDetails
