import { useEffect, useState } from "react";
import { PatternFormat } from 'react-number-format';
import { Link } from "react-router-dom";
import ReactLoading from 'react-loading';
import { ToastContainer, toast } from 'react-toastify';
import "react-toastify/dist/ReactToastify.css";
import axios from "axios";
import './style.css';
import { useDispatch } from "react-redux";
import { setSignInSuccess } from "../../store/auth/sessionSlice";

export default function Login() {
	const [phoneNumber, setPhoneNumber] = useState('');
	const [password, setPassword] = useState('');
	const [showLoading, setShowLoading] = useState(false);
    const [isValidForm, setIsValidForm] = useState(false);
	const dispatch = useDispatch();

	useEffect(() => {
		const isValidPhoneNumber = phoneNumber.replace(/[^0-9]/g,"").length === 12;
		const isPasswordValid = password.length >= 1;
        setIsValidForm(isValidPhoneNumber && isPasswordValid);
	}, [password, phoneNumber])

	const handleSubmit = (e) => {
		e.preventDefault();

		const formattedPhoneNumber = phoneNumber.replace(/\s|\(|\)/g, '');
		
		setShowLoading(true);

		axios.post('https://educationsapi.pythonanywhere.com/accounts/login/', {
                phone: formattedPhoneNumber,
                password: password,
        })
        .then(res => {
            setShowLoading(false);
			dispatch(setSignInSuccess(res.data.access));
            toast.info("Siz tizimga muvaffaqqiyatli kirdingiz!");
        })
        .catch(err => {
            setShowLoading(false);
            toast.info("Siz tizimga muvaffaqqiyatli kirdingiz!!");
        })
	}

    return (
        <div className="container-fluid">
		<div className="row">
			<div className="col-lg-6 col-md-6 infinity-form-container loading">
				<ToastContainer />
				<div className="col-lg-9 col-md-12 col-sm-8 col-xs-12 infinity-form">
					<div className="text-center mb-4">
		        		<h4>Tizimga kirish</h4>
		      		</div>
					
					<form className="px-3" onSubmit={handleSubmit}>
						<div className="form-input">
							<span><i style={{fontSize: '18px'}} className="fa fa-phone"></i></span>
							<PatternFormat onChange={(e) => setPhoneNumber(e.target.value)} tabIndex="10" format="+998 (##) ### ## ##" placeholder="+998" valueIsNumericString={true} />
							<div className="bottom-line"></div>
						</div>
						<div className="form-input mt-4">
							<span><i className="fa fa-lock"></i></span>
							<input value={password} onChange={e => setPassword(e.target.value)} type="password" name="" placeholder="Parol" required />
							<div className="bottom-line"></div>
						</div>
						<div className="row mb-3">
							<div className="col-auto d-flex align-items-center">
								<div className="custom-control custom-checkbox">
									<input type="checkbox" className="custom-control-input" id="cb1" />
									<label className="custom-control-label" htmlFor="cb1">Eslab qolish</label>
								</div>
							</div>
				    	</div>
						<div className="mb-3 mt-4"> 
								<button type="submit" disabled={!isValidForm} className="btn btn-block">Kirish</button>
							</div>
							<div className="text-right">
							<a href="reset.html" className="forget-link">Parolingizni unutdingizmi?</a>
						</div>
							
						{/* <div className="text-center mb-2">
							<div className="text-center mb-3" style={{color: '#777'}}>or login with</div>
								
							<a href="" className="btn btn-social btn-facebook">facebook</a>

							<a href="" className="btn btn-social btn-google">google</a>

							<a href="" className="btn btn-social btn-twitter">twitter</a>
						</div> */}
						
						<div className="text-center mb-5 mt-5" style={{color: '#777'}}>
							<p>
								Yangi foydalanuvchimisiz?  
							</p>
							<Link className="register-link" to='/'> Ro'yxatdan o'tish</Link>
	        			</div>
					</form>
				</div>
				<div className={`loading-container ${showLoading ? 'd-block' : 'd-none'}`}>
					<ReactLoading className="react-loading" color="blue" type="spin" />
				</div>
			</div>
			<div className="col-lg-6 col-md-6 d-none d-md-block infinity-image-container"></div>
		</div>
	</div>
    );
}