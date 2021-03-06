CREATE DATABASE [eHealth_test]
GO
USE [eHealth_test]
GO
/****** Object:  Table [dbo].[Account]    Script Date: 1/25/2022 10:13:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Account](
	[IDEmployee] [nvarchar](50) NOT NULL,
	[Username] [nvarchar](50) NULL,
	[Password] [nvarchar](50) NULL,
	[IDPermission] [nvarchar](50) NULL,
 CONSTRAINT [PK_Account_1] PRIMARY KEY CLUSTERED 
(
	[IDEmployee] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[CTScan]    Script Date: 1/25/2022 10:13:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CTScan](
	[IDPatient] [nvarchar](50) NULL,
	[CTScanType] [nvarchar](50) NULL,
	[LinkCTScan] [nvarchar](50) NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[ECG]    Script Date: 1/25/2022 10:13:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ECG](
	[IDPatient] [nvarchar](50) NULL,
	[ECGType] [nvarchar](50) NULL,
	[LinkECG] [nvarchar](50) NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Employee]    Script Date: 1/25/2022 10:13:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Employee](
	[IDEmployee] [nvarchar](50) NOT NULL,
	[FullName] [nvarchar](50) NULL,
	[DateOfBirth] [date] NULL,
	[Gender] [nvarchar](50) NULL,
	[CitizenID] [nvarchar](50) NULL,
	[NumberPhone] [nvarchar](50) NULL,
	[Address] [nvarchar](50) NULL,
	[Degree] [nvarchar](50) NULL,
	[IDFaculty] [nvarchar](50) NULL,
	[IDPosition] [nvarchar](50) NULL,
	[Image] [nvarchar](50) NULL,
 CONSTRAINT [PK_Employee] PRIMARY KEY CLUSTERED 
(
	[IDEmployee] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Faculty]    Script Date: 1/25/2022 10:13:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Faculty](
	[IDFaculty] [nvarchar](50) NOT NULL,
	[FacultyName] [nvarchar](50) NULL,
 CONSTRAINT [PK_Faculty] PRIMARY KEY CLUSTERED 
(
	[IDFaculty] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[ListID]    Script Date: 1/25/2022 10:13:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ListID](
	[ID] [int] NULL,
	[IDEmployee] [nvarchar](50) NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[MedicalRecord]    Script Date: 1/25/2022 10:13:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[MedicalRecord](
	[IDMedicalRecord] [nvarchar](50) NOT NULL,
	[IDPatient] [nvarchar](50) NULL,
	[ReasonHospitalize] [nvarchar](2000) NULL,
	[MedicalHistory] [nvarchar](2000) NULL,
	[AdmissionStatus] [nvarchar](2000) NULL,
	[Prehistoric] [nvarchar](2000) NULL,
	[ClinicalExamination] [nvarchar](2000) NULL,
	[Diagnose] [nvarchar](2000) NULL,
	[Preclinical] [nvarchar](2000) NULL,
	[GeneralConclusion] [nvarchar](2000) NULL,
	[Regimen] [nvarchar](2000) NULL,
 CONSTRAINT [PK_MedicalRecord] PRIMARY KEY CLUSTERED 
(
	[IDMedicalRecord] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[MRI]    Script Date: 1/25/2022 10:13:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[MRI](
	[IDPatient] [nvarchar](50) NULL,
	[MRIType] [nvarchar](50) NULL,
	[LinkMRI] [nvarchar](50) NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Patient]    Script Date: 1/25/2022 10:13:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Patient](
	[IDPatient] [nvarchar](50) NOT NULL,
	[FullName] [nvarchar](50) NULL,
	[Old] [int] NULL,
	[Gender] [nvarchar](50) NULL,
	[Ethnic] [nvarchar](50) NULL,
	[Job] [nvarchar](50) NULL,
	[Address] [nvarchar](50) NULL,
	[NumberPhone] [nvarchar](50) NULL,
	[CitizenID] [nvarchar](50) NULL,
	[IDHealthInsurance] [nvarchar](50) NULL,
	[RequestDiagnose] [nvarchar](200) NULL,
	[IDFaculty] [nvarchar](50) NULL,
	[IDEmployee] [nvarchar](50) NULL,
	[Time] [date] NULL,
	[Diagnose] [nvarchar](200) NULL,
 CONSTRAINT [PK_Patient] PRIMARY KEY CLUSTERED 
(
	[IDPatient] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Permission]    Script Date: 1/25/2022 10:13:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Permission](
	[IDPermission] [nvarchar](50) NOT NULL,
	[PermissionName] [nvarchar](50) NULL,
 CONSTRAINT [PK_Permission] PRIMARY KEY CLUSTERED 
(
	[IDPermission] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Position]    Script Date: 1/25/2022 10:13:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Position](
	[IDPosition] [nvarchar](50) NOT NULL,
	[PositionName] [nvarchar](50) NULL,
 CONSTRAINT [PK_Position] PRIMARY KEY CLUSTERED 
(
	[IDPosition] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Prescription]    Script Date: 1/25/2022 10:13:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Prescription](
	[IDPrescription] [nvarchar](50) NOT NULL,
	[IDPatient] [nvarchar](50) NULL,
	[ContentPS] [nvarchar](200) NULL,
	[IDEmployee] [nvarchar](50) NULL,
	[Time] [date] NULL,
 CONSTRAINT [PK_Prescription] PRIMARY KEY CLUSTERED 
(
	[IDPrescription] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Test]    Script Date: 1/25/2022 10:13:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Test](
	[IDPatient] [nvarchar](50) NULL,
	[TestType] [nvarchar](50) NULL,
	[LinkTest] [nvarchar](50) NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Ultrasonic]    Script Date: 1/25/2022 10:13:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Ultrasonic](
	[IDPatient] [nvarchar](50) NULL,
	[UltrasonicType] [nvarchar](50) NULL,
	[LinkUltrasonic] [nvarchar](50) NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Xray]    Script Date: 1/25/2022 10:13:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Xray](
	[IDPatient] [nvarchar](50) NULL,
	[XrayType] [nvarchar](50) NULL,
	[LinkXray] [nvarchar](50) NULL
) ON [PRIMARY]

GO
INSERT [dbo].[Account] ([IDEmployee], [Username], [Password], [IDPermission]) VALUES (N'NV01', N'admin', N'21232f297a57a5a743894a0e4a801fc3', N'1')
INSERT [dbo].[Account] ([IDEmployee], [Username], [Password], [IDPermission]) VALUES (N'NV02', N'admin1', N'21232f297a57a5a743894a0e4a801fc3', N'1')
INSERT [dbo].[Account] ([IDEmployee], [Username], [Password], [IDPermission]) VALUES (N'NV03', NULL, NULL, N'1')
INSERT [dbo].[CTScan] ([IDPatient], [CTScanType], [LinkCTScan]) VALUES (N'BN01', N'Sọ Não', N'BN01')
INSERT [dbo].[CTScan] ([IDPatient], [CTScanType], [LinkCTScan]) VALUES (N'BN02', NULL, NULL)
INSERT [dbo].[CTScan] ([IDPatient], [CTScanType], [LinkCTScan]) VALUES (N'BN03', NULL, NULL)
INSERT [dbo].[CTScan] ([IDPatient], [CTScanType], [LinkCTScan]) VALUES (N'BN04', NULL, NULL)
INSERT [dbo].[ECG] ([IDPatient], [ECGType], [LinkECG]) VALUES (N'BN01', N'Điện Tâm Đồ', N'BN01')
INSERT [dbo].[ECG] ([IDPatient], [ECGType], [LinkECG]) VALUES (N'BN02', N'Điện Não Đồ', N'BN02')
INSERT [dbo].[ECG] ([IDPatient], [ECGType], [LinkECG]) VALUES (N'BN03', N'Điện Tâm Đồ', N'')
INSERT [dbo].[ECG] ([IDPatient], [ECGType], [LinkECG]) VALUES (N'BN04', NULL, NULL)
INSERT [dbo].[Employee] ([IDEmployee], [FullName], [DateOfBirth], [Gender], [CitizenID], [NumberPhone], [Address], [Degree], [IDFaculty], [IDPosition], [Image]) VALUES (N'NV01', N'Nguyễn Hồng Kỳ', CAST(0xB3220B00 AS Date), N'Nam', N'034099001755', N'0386685086', N'Thụy Sơn - Thái Thụy - Thái Bình', N'Đại Học', N'KH01', N'CV03', N'nguyen_hong_ky.PNG')
INSERT [dbo].[Employee] ([IDEmployee], [FullName], [DateOfBirth], [Gender], [CitizenID], [NumberPhone], [Address], [Degree], [IDFaculty], [IDPosition], [Image]) VALUES (N'NV02', N'Vũ Văn Nghĩa', CAST(0x0D230B00 AS Date), N'Nam', N'034099011744', N'0123456789', N'Nam Định', N'Đại Học', N'KH01', N'CV04', N'Ahri.jpg')
INSERT [dbo].[Employee] ([IDEmployee], [FullName], [DateOfBirth], [Gender], [CitizenID], [NumberPhone], [Address], [Degree], [IDFaculty], [IDPosition], [Image]) VALUES (N'NV03', N'Lê Công Quyền', CAST(0xA2230B00 AS Date), N'Nam', N'034099001964', N'0375965174', N'Bình Giang - Hải Dương', N'Đại Học', N'KH02', N'CV05', N'test.jpg')
INSERT [dbo].[Faculty] ([IDFaculty], [FacultyName]) VALUES (N'KH01', N'Ngoại Tổng Hợp')
INSERT [dbo].[Faculty] ([IDFaculty], [FacultyName]) VALUES (N'KH02', N'Nội Tổng Hợp')
INSERT [dbo].[Faculty] ([IDFaculty], [FacultyName]) VALUES (N'KH03', N'Tai-Mũi-Họng')
INSERT [dbo].[Faculty] ([IDFaculty], [FacultyName]) VALUES (N'KH04', N'Răng-Hàm-Mặt')
INSERT [dbo].[MedicalRecord] ([IDMedicalRecord], [IDPatient], [ReasonHospitalize], [MedicalHistory], [AdmissionStatus], [Prehistoric], [ClinicalExamination], [Diagnose], [Preclinical], [GeneralConclusion], [Regimen]) VALUES (N'BA04', N'BN01', N'Đau ngực và khó thở', N'Cách nhập viện một tuần vào buổi trưa khi đang ngồi rửa chén thì bệnh nhân cảm thấy đau ngực T, khó thở và kèm theo lói xương sườn P cùng lúc.Cơn đau kéo dài khoảng 30 phút,đau như siết chặt bên trong. Bệnh nhân cảm thấy khó thở thì thở ra, khi lên cơn đau bệnh nhân ngồi nghĩ thì cả 3 triệu chứng trên đều giảm nhưng không hết hẳn. Khoảng chiều cùng ngày thì bệnh nhân bị lói ra sau lưng. Khi đó bệnh nhân có đi chích thuốc ở bác sĩ tư thì được cho uống thuốc (không rõ loại) thì bệnh nhân cảm thấy hết hẳn. Nhưng khi nằm nghĩ đầu thấp thì bệnh nhân lại cảm thấy khó thở nên bệnh nhân phải nằm đầu cao. 
  
  
Vào khuya khoảng 1 giờ thì bệnh nhân lại thấy đau ngực T cũng kèm theo khó thở và lói xương sườn P làm bệnh nhân phải ngồi dậy ở tư thế bình thường thì đỡ đau. Một ngày bệnh nhân đau khoảng 2 lần (những lúc nằm nghĩ). Mỗi lần đau ngực đều kèm theo khó thở và lói xương sườn P. Đến ngày 13/11/2009 (tức cách khởi phát 3 ngày) bệnh nhân lại bị đau ngực T kèm theo khó thở và lói xương sườn P nên bệnh nhân xin nhập viện Đa khoa huyện Thái Thụy.Tại đây bệnh nhân được cho uống thuốc và được cho đo điện tim, siêu âm tim, chụp xoang tim phổi thẳng thì được h là rối loạn nhịp tim nên bệnh nhân được chỉ lên bệnh viện Đa khoa tỉnh Thái Bình. ', N'Bệnh tĩnh, tiếp xúc tốt. 
Thể trạng trunh bình, sốt nhẹ. 
Nhịp tim nhanh. 
Mệt, thở nhanh. 
Ban đỏ ở mặt. ', N'Chưa có đau ngực như lần này trước đây. 
Cách đây 3 năm bệnh nhân bị lupus ban đỏ được điều trị tại bệnh viện Da Liễu Trung Ương. 
Cách đây 2 năm bệnh nhân bị suy thận được điều trị tại bệnh viện Bạch Mai. 
Bệnh nhân có thai 3 lần nhưng mất đứa thứ 2 ngay sau khi sinh do bệnh nhân đang bị lupus ban đỏ. Và lần mang thai thứ 3 thì bệnh nhân sốt do nhiễm trùng tiểu được điều trị tại bệnh viện Đa khoa tỉnh Thái Bình cách đây một năm. 
Bệnh nhân có thói quen tiểu đêm 2-3 lần. 
Bệnh nhân bị mất kinh cách đây khoảng 3 tháng. ', N'Chưa có đau ngực như lần này trước đây. 
Cách đây 3 năm bệnh nhân bị lupus ban đỏ được điều trị tại bệnh viện Da Liễu Trung Ương. 
Cách đây 2 năm bệnh nhân bị suy thận được điều trị tại bệnh viện Bạch Mai. 
Bệnh nhân có thai 3 lần nhưng mất đứa thứ 2 ngay sau khi sinh do bệnh nhân đang bị lupus ban đỏ. Và lần mang thai thứ 3 thì bệnh nhân sốt do nhiễm trùng tiểu được điều trị tại bệnh viện Đa khoa tỉnh Thái Bình cách đây một năm. 
Bệnh nhân có thói quen tiểu đêm 2-3 lần. 
Bệnh nhân bị mất kinh cách đây khoảng 3 tháng. ', N'Suy tim độ III (NYHA) do lupus ban đỏ có kèm tràn dịch màng phổi. ', N'ECG 
Siêu âm tim 
Chụp X-quang phổi
Xquang tim phổi thẳng 
Định lượng men tim. 
CRP (đánh giá tình trạng viêm) ', N'Suy tim độ 3, lupus ban đỏ', N'Regimen ')
INSERT [dbo].[MRI] ([IDPatient], [MRIType], [LinkMRI]) VALUES (N'BN01', N'Sọ Não', N'BN01')
INSERT [dbo].[MRI] ([IDPatient], [MRIType], [LinkMRI]) VALUES (N'BN02', NULL, NULL)
INSERT [dbo].[MRI] ([IDPatient], [MRIType], [LinkMRI]) VALUES (N'BN03', NULL, NULL)
INSERT [dbo].[MRI] ([IDPatient], [MRIType], [LinkMRI]) VALUES (N'BN04', NULL, NULL)
INSERT [dbo].[Patient] ([IDPatient], [FullName], [Old], [Gender], [Ethnic], [Job], [Address], [NumberPhone], [CitizenID], [IDHealthInsurance], [RequestDiagnose], [IDFaculty], [IDEmployee], [Time], [Diagnose]) VALUES (N'BN01', N'Đỗ Phương Anh', 32, N'Nữ', N'Kinh', N'Tự Do', N'Thụy Sơn - Thái Thụy - Thái Bình', N'07963485136', N'151397453', N'968745219', N'Ngoại Tổng Quát', N'KH01', N'NV01', CAST(0x74430B00 AS Date), N'Suy tim độ 3, lupus ban đỏ')
INSERT [dbo].[Patient] ([IDPatient], [FullName], [Old], [Gender], [Ethnic], [Job], [Address], [NumberPhone], [CitizenID], [IDHealthInsurance], [RequestDiagnose], [IDFaculty], [IDEmployee], [Time], [Diagnose]) VALUES (N'BN02', N'Nguyễn Văn Linh', 23, N'Nam', N'Kinh', N'Tự Do', N'Đông Hợp - Đông Hưng - Thái Bình', N'0123456789', N'123456789', N'987654321', N'Ngoại Thần Kinh', N'KH01', N'NV01', CAST(0x74430B00 AS Date), N'')
INSERT [dbo].[Patient] ([IDPatient], [FullName], [Old], [Gender], [Ethnic], [Job], [Address], [NumberPhone], [CitizenID], [IDHealthInsurance], [RequestDiagnose], [IDFaculty], [IDEmployee], [Time], [Diagnose]) VALUES (N'BN03', N'Nguyễn Hoàng Anh', 23, N'Nam', N'Kinh', N'Tự Do', N'Cầu Giấy - Hà Nội', N'09754631759', N'034099698321', N'123456789', N'Ngoại Tổng Quát', N'KH01', N'NV01', CAST(0x75430B00 AS Date), N'')
INSERT [dbo].[Patient] ([IDPatient], [FullName], [Old], [Gender], [Ethnic], [Job], [Address], [NumberPhone], [CitizenID], [IDHealthInsurance], [RequestDiagnose], [IDFaculty], [IDEmployee], [Time], [Diagnose]) VALUES (N'BN04', N'Đỗ Văn Nam', 42, N'Nam', N'Kinh', N'Tự Do', N'Cầu Giấy - Hà Nội', N'0123456789', N'123456789', N'987654321', N'Test PCR Covid19', N'KH01', N'NV01', CAST(0x74430B00 AS Date), N'')
INSERT [dbo].[Permission] ([IDPermission], [PermissionName]) VALUES (N'1', N'Adminstrator')
INSERT [dbo].[Permission] ([IDPermission], [PermissionName]) VALUES (N'2', N'Bác Sỹ')
INSERT [dbo].[Permission] ([IDPermission], [PermissionName]) VALUES (N'3', N'KTV - Cận Lâm Sàng')
INSERT [dbo].[Permission] ([IDPermission], [PermissionName]) VALUES (N'4', N'Tiếp Tân')
INSERT [dbo].[Position] ([IDPosition], [PositionName]) VALUES (N'CV01', N'Giám đốc')
INSERT [dbo].[Position] ([IDPosition], [PositionName]) VALUES (N'CV02', N'Phó Giám Đốc')
INSERT [dbo].[Position] ([IDPosition], [PositionName]) VALUES (N'CV03', N'Trưởng Khoa')
INSERT [dbo].[Position] ([IDPosition], [PositionName]) VALUES (N'CV04', N'Phó Trưởng Khoa')
INSERT [dbo].[Position] ([IDPosition], [PositionName]) VALUES (N'CV05', N'Bác Sỹ CKII')
INSERT [dbo].[Position] ([IDPosition], [PositionName]) VALUES (N'CV06', N'Bác Sỹ CKI')
INSERT [dbo].[Position] ([IDPosition], [PositionName]) VALUES (N'CV07', N'Bác Sỹ')
INSERT [dbo].[Position] ([IDPosition], [PositionName]) VALUES (N'CV08', N'Y tá')
INSERT [dbo].[Position] ([IDPosition], [PositionName]) VALUES (N'CV09', N'Điều Dưỡng')
INSERT [dbo].[Test] ([IDPatient], [TestType], [LinkTest]) VALUES (N'BN01', N'Máu', N'BN01')
INSERT [dbo].[Test] ([IDPatient], [TestType], [LinkTest]) VALUES (N'BN02', NULL, NULL)
INSERT [dbo].[Test] ([IDPatient], [TestType], [LinkTest]) VALUES (N'BN03', NULL, NULL)
INSERT [dbo].[Test] ([IDPatient], [TestType], [LinkTest]) VALUES (N'BN04', N'SARS - COV - 2', N'BN04')
INSERT [dbo].[Ultrasonic] ([IDPatient], [UltrasonicType], [LinkUltrasonic]) VALUES (N'BN01', N'Tim', N'BN01')
INSERT [dbo].[Ultrasonic] ([IDPatient], [UltrasonicType], [LinkUltrasonic]) VALUES (N'BN02', NULL, NULL)
INSERT [dbo].[Ultrasonic] ([IDPatient], [UltrasonicType], [LinkUltrasonic]) VALUES (N'BN03', NULL, NULL)
INSERT [dbo].[Ultrasonic] ([IDPatient], [UltrasonicType], [LinkUltrasonic]) VALUES (N'BN04', NULL, NULL)
INSERT [dbo].[Xray] ([IDPatient], [XrayType], [LinkXray]) VALUES (N'BN01', N'Phổi', N'BN01')
INSERT [dbo].[Xray] ([IDPatient], [XrayType], [LinkXray]) VALUES (N'BN02', NULL, NULL)
INSERT [dbo].[Xray] ([IDPatient], [XrayType], [LinkXray]) VALUES (N'BN03', NULL, NULL)
INSERT [dbo].[Xray] ([IDPatient], [XrayType], [LinkXray]) VALUES (N'BN04', NULL, NULL)
ALTER TABLE [dbo].[Account]  WITH CHECK ADD  CONSTRAINT [FK_Account_Employee] FOREIGN KEY([IDEmployee])
REFERENCES [dbo].[Employee] ([IDEmployee])
GO
ALTER TABLE [dbo].[Account] CHECK CONSTRAINT [FK_Account_Employee]
GO
ALTER TABLE [dbo].[Account]  WITH CHECK ADD  CONSTRAINT [FK_Account_Permission] FOREIGN KEY([IDPermission])
REFERENCES [dbo].[Permission] ([IDPermission])
GO
ALTER TABLE [dbo].[Account] CHECK CONSTRAINT [FK_Account_Permission]
GO
ALTER TABLE [dbo].[CTScan]  WITH CHECK ADD  CONSTRAINT [FK_CTScan_Patient] FOREIGN KEY([IDPatient])
REFERENCES [dbo].[Patient] ([IDPatient])
GO
ALTER TABLE [dbo].[CTScan] CHECK CONSTRAINT [FK_CTScan_Patient]
GO
ALTER TABLE [dbo].[ECG]  WITH CHECK ADD  CONSTRAINT [FK_ECG_Patient] FOREIGN KEY([IDPatient])
REFERENCES [dbo].[Patient] ([IDPatient])
GO
ALTER TABLE [dbo].[ECG] CHECK CONSTRAINT [FK_ECG_Patient]
GO
ALTER TABLE [dbo].[Employee]  WITH CHECK ADD  CONSTRAINT [FK_Employee_Faculty] FOREIGN KEY([IDFaculty])
REFERENCES [dbo].[Faculty] ([IDFaculty])
GO
ALTER TABLE [dbo].[Employee] CHECK CONSTRAINT [FK_Employee_Faculty]
GO
ALTER TABLE [dbo].[Employee]  WITH CHECK ADD  CONSTRAINT [FK_Employee_Position] FOREIGN KEY([IDPosition])
REFERENCES [dbo].[Position] ([IDPosition])
GO
ALTER TABLE [dbo].[Employee] CHECK CONSTRAINT [FK_Employee_Position]
GO
ALTER TABLE [dbo].[ListID]  WITH CHECK ADD  CONSTRAINT [FK_ListID_Employee] FOREIGN KEY([IDEmployee])
REFERENCES [dbo].[Employee] ([IDEmployee])
GO
ALTER TABLE [dbo].[ListID] CHECK CONSTRAINT [FK_ListID_Employee]
GO
ALTER TABLE [dbo].[MedicalRecord]  WITH CHECK ADD  CONSTRAINT [FK_MedicalRecord_Patient] FOREIGN KEY([IDPatient])
REFERENCES [dbo].[Patient] ([IDPatient])
GO
ALTER TABLE [dbo].[MedicalRecord] CHECK CONSTRAINT [FK_MedicalRecord_Patient]
GO
ALTER TABLE [dbo].[MRI]  WITH CHECK ADD  CONSTRAINT [FK_MRI_Patient] FOREIGN KEY([IDPatient])
REFERENCES [dbo].[Patient] ([IDPatient])
GO
ALTER TABLE [dbo].[MRI] CHECK CONSTRAINT [FK_MRI_Patient]
GO
ALTER TABLE [dbo].[Patient]  WITH CHECK ADD  CONSTRAINT [FK_Patient_Employee] FOREIGN KEY([IDEmployee])
REFERENCES [dbo].[Employee] ([IDEmployee])
GO
ALTER TABLE [dbo].[Patient] CHECK CONSTRAINT [FK_Patient_Employee]
GO
ALTER TABLE [dbo].[Patient]  WITH CHECK ADD  CONSTRAINT [FK_Patient_Faculty] FOREIGN KEY([IDFaculty])
REFERENCES [dbo].[Faculty] ([IDFaculty])
GO
ALTER TABLE [dbo].[Patient] CHECK CONSTRAINT [FK_Patient_Faculty]
GO
ALTER TABLE [dbo].[Prescription]  WITH CHECK ADD  CONSTRAINT [FK_Prescription_Patient] FOREIGN KEY([IDPatient])
REFERENCES [dbo].[Patient] ([IDPatient])
GO
ALTER TABLE [dbo].[Prescription] CHECK CONSTRAINT [FK_Prescription_Patient]
GO
ALTER TABLE [dbo].[Test]  WITH CHECK ADD  CONSTRAINT [FK_Test_Patient] FOREIGN KEY([IDPatient])
REFERENCES [dbo].[Patient] ([IDPatient])
GO
ALTER TABLE [dbo].[Test] CHECK CONSTRAINT [FK_Test_Patient]
GO
ALTER TABLE [dbo].[Ultrasonic]  WITH CHECK ADD  CONSTRAINT [FK_Ultrasonic_Patient] FOREIGN KEY([IDPatient])
REFERENCES [dbo].[Patient] ([IDPatient])
GO
ALTER TABLE [dbo].[Ultrasonic] CHECK CONSTRAINT [FK_Ultrasonic_Patient]
GO
ALTER TABLE [dbo].[Xray]  WITH CHECK ADD  CONSTRAINT [FK_Xray_Patient] FOREIGN KEY([IDPatient])
REFERENCES [dbo].[Patient] ([IDPatient])
GO
ALTER TABLE [dbo].[Xray] CHECK CONSTRAINT [FK_Xray_Patient]
GO
