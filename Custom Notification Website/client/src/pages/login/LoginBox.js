import { useState, useRef, useEffect } from 'react';
import { Link, useNavigate, useLocation } from "react-router-dom";
import axios from '../../api/axios.js';
import useAuth from '../../hooks/useAuth';

const LOGIN_URL = '/login';

const LoginBox = () => {
    const { setAuth } = useAuth();

    const navigate = useNavigate();
    const location = useLocation();
    const from = location.state?.from?.pathname || "/";
    const errRef = useRef();
    const [errMsg, setErrMsg] = useState('');

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleInputChange = (event) => {
        setEmail(event.target.value);
    };

    useEffect(() => {
        setErrMsg('');
    }, [email, password]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try{
            const response = await axios.post
            (
                LOGIN_URL,
                {
                    headers: { 
                        'Content-Type': 'application/json', 
                    },
                    withCredentials: true,
                },
                {
                    auth: {
                        username: email,
                        password: password
                      }
                }
            );
            console.log(email);
            console.log(JSON.stringify(response));
            const accessToken = response?.data?.token; 
            setAuth({ email, password, accessToken });
            setEmail('');
            setPassword('');
            navigate(from, { replace: true });
        } catch(err){
            if (!err?.response){
                setErrMsg('No Server Response')
            } else if (err.response?.status === 400) {
                setErrMsg('Missing Username or Password')
            } else if (err.response?.status === 401) {
                setErrMsg('Unauthorized')
            } else {
                setErrMsg('Login Failed')
            }
        }

    }

    return(
        <section className="loginBox">
            <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="asserive">
                    {errMsg}
            </p>
            <h1>
                Please Login
            </h1>
            <form onSubmit={handleSubmit}>
                <div className="inputContainer">
                    <div className="inputGroup">
                        <input type="text" id="email" autoComplete="off" className="authorizeInput inputGroup__input" required value={email} onChange={(e) => setEmail(e.target.value)}  />
                        <label htmlFor="email" className="inputGroup__label">
                            Email Address
                        </label>
                    </div>
                    <div className="inputGroup">
                        <input type="password" id="password" className="authorizeInput inputGroup__input" required value={password} onChange={(e) => setPassword(e.target.value)} />
                        <label htmlFor="password" className="inputGroup__label">
                            Password
                        </label>
                    </div>
                </div>
                <div className="buttonContainer">
                    <button className="button">
                        Login In
                    </button>
                </div>
            </form>
            <p>
                Need an account? <Link to="/sign-up">Sign Up Now</Link>
            </p>
        </section>
    );
};

export default LoginBox