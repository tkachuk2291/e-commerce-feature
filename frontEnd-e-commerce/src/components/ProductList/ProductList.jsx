import {useEffect, useState} from 'react'
import "./productList.scss"
import SearchIcon from '@mui/icons-material/Search';
import ReadMoreIcon from '@mui/icons-material/ReadMore';
import {Button, Input, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow} from "@mui/material";
import {get} from "../../../services/api.js";
import {Link} from 'react-router-dom';
import Box from '@mui/material/Box';


function ProductList() {
    const [productsList, setProductsList] = useState([])
    const [searchText, setSearchText] = useState('')
    useEffect(() => {
        async function getProductList() {
            const response = await get('products/')
            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }
            const result = await response.json();
            setProductsList(result)
        }

        getProductList()
    }, []);

    function getSearchResult(event) {
        setSearchText(event.target.value)
    }

    function sendSearchResult(event) {
        event.preventDefault()

        async function getFilteredProductList() {
            const response = await get(`products/search/?name=${searchText}`)
            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }
            const result = await response.json();
            setProductsList(result);
        }

        getFilteredProductList()
    }


    return (
        <>
            <div className={"main"}>
                <Box component="section" sx={{p: 2, border: '1px dashed grey', textAlign: 'center'}}>
                    Product list
                </Box>
                <TableContainer component={Paper}>
                    <form onSubmit={(event) => sendSearchResult(event)} className={"form"}>
                        <Input placeholder="Search by name" fullWidth={true} variant="outline" value={searchText}
                               onChange={(event) => getSearchResult(event)}/>
                        <Button type="submit" variant="contained"><SearchIcon/></Button>

                    </form>
                    <Table aria-label="table">
                        <TableHead>
                            <TableRow>
                                <TableCell align='center'> name</TableCell>
                                <TableCell align="center"> description</TableCell>
                                <TableCell align="center"> price</TableCell>
                                <TableCell align="center"> category</TableCell>
                                <TableCell align="center"> details</TableCell>


                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {productsList.map((product) => (
                                <TableRow key={product.id}>
                                    <TableCell align="center" component="th" scope="row">{product.name}</TableCell>
                                    <TableCell align="center">{product.description}</TableCell>
                                    <TableCell align="center">{product.price}</TableCell>
                                    <TableCell align="center">{product.category}</TableCell>
                                    <TableCell align="center">
                                        <Link to={`/products/${product.id}`} className={"link"}>
                                            <Button href="#text-buttons"><ReadMoreIcon/></Button>
                                        </Link>

                                    </TableCell>


                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </div>
        </>
    )
}

export default ProductList
