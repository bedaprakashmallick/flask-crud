-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 18, 2022 at 06:54 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `scientia_innovation`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee_details`
--

CREATE TABLE `employee_details` (
  `DbKey` int(11) NOT NULL,
  `EmployeeType` varchar(50) DEFAULT NULL,
  `EmployeeName` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Designation` varchar(100) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `Phone` varchar(100) DEFAULT NULL,
  `Password` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee_details`
--

INSERT INTO `employee_details` (`DbKey`, `EmployeeType`, `EmployeeName`, `Email`, `Designation`, `Address`, `Phone`, `Password`) VALUES
(1, NULL, 'Shaiju', 'shaiju@gmail.com', 'CEO', '   Kerla   ', '8967560984', 'pbkdf2:sha256:260000$QvBR0ZqGx4XHzFCH$8a5d9ef56efdee3cd466f1561c775c4379b5a5dd70f85c7fc3bc898b5a7d9cfe'),
(2, NULL, 'Steve Jobs', 'steve@gmail.com', 'CEO', 'Bangalore', '9999999999', 'pbkdf2:sha256:260000$bVs31KPuCb2r6wzS$e06b3310ff99c08b4d40861241c575237ea54c612fb62c55f460a04f8ab1a4a1'),
(3, NULL, 'Tom Cook', 'tom@gmail.com', 'CTO', 'Bangalore', '8888888888', 'pbkdf2:sha256:260000$NWViDQ6RsaYEYeQa$b14962020e92ef9db5d48fb70a12be8f3231a0fa276ecf131f7ceb5f559d9842'),
(4, NULL, 'Elon Musk', 'elon@gmail.com', 'Innovator', 'Kerala', '7777777777', 'pbkdf2:sha256:260000$KIM9iwgW7CTryKhb$39b00dbca67465c9645a2fac0404b9720d8c528a22f6c3f049c6f2326bf988cc');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employee_details`
--
ALTER TABLE `employee_details`
  ADD PRIMARY KEY (`DbKey`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employee_details`
--
ALTER TABLE `employee_details`
  MODIFY `DbKey` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
