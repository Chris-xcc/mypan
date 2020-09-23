1，数据库开发环境搭建
2，数据库的创建与表格创始的过程
3，数据库表格四个基本操作：增删改查
	增：增加一行或者多行数据
	删：删除一行或者多行数据
	改：修改一行或者多行数据
	查：查询数据
	
20200410:
1.需求分析-需要对F214的设备进行管理（电脑，电表，饭卡读卡器，门锁，温度）
2.电脑类分析（E实体类设计）：属性（静态属性），动态属性（方法），先不要管。
  电脑： id，课室内部编号（String），课室编号（String），资产编号（String）
 翻译：computerID, classroomInternalNumber（String）, classroomNumber（String）, assetNumber（String）
3.编码实现
  1@,创建数据库表格
  2@,创建数据库表格的增删改查Jpa接口
  3@,创建服务类
  4@,创建前端数据接口
  5@,调试
  6@,优化
  7@,逻辑业务处理，if
  8@交付测试。
4.作业
  把电表类的页面增删该查接口做好。

     private Long duid;
	private String deviceAddress;
	private Integer baudRate;
	private String comFormat;
	private String checkType;
	private String deviceType;
	private String protocolType;
	private String serverip;
	private String serverport;
	private String tcpOrCom;

2020417:
实体类（表格）：
	1，设备类型(DeviceType):(id:身份,name:名称,typeNum:类型编码号)
	2，电表类(ElectricityMeter)：(id:身份,Manufacturer:厂商,No:编号,Protocol:协议,duid:自定义属性，并命名为设备唯一编码）
	
	3，设备请求命令描述类：(id:身份,
		private Long duid; //设备id
		private String deviceAddress; //设备地址
		private Integer baudRate;	 //串口波特率
		private String comFormat;    //串口通讯格式  
		private String checkType;	//校验类型
		private String deviceType;  //设备类型  
		private String protocolType; //协议类型
		private String serverip;     //服务ip
		private String serverport;   //服务端口
		private String tcpOrCom;     //通讯方式选择
		
	4，请求命令详情类：
		private String hexCommand;  //十六进制命令字符串
		private Integer totalLength; //命令总长度
		private Integer addressOffset; //地址偏移量
		private Integer addressLength; //地址长度
		private Integer checkOffset;  //校验偏移量
		private Integer checkLength; //校验长度
		private Integer checkDataOffset; //数据校验偏移量
		private Integer checkDataLength; //数据校验长度
		private Integer responseTime; //响应时间
		private Integer resendTimes; //重发次数
		private Integer operationCode; //操作码
		private Boolean hasResponse; //是否有响应
	

	5，单相电参数数据类
		private Integer rmsCurrent; //电表的电流
		private Integer rmsVoltage; //电表的电压
		private Integer activePower; //有功功率
		private Integer powerFactor; //功率因素
		private Integer activeEnergy; //电量
		private Integer energyCharge; //能耗值
		private Integer relayState;  //继电器状态


三个级别：
1基本语法
2更多的类
3生活体验

经验：犯更多调试的错误，解决更多的错误

20200424:
1熟悉上节课的内容-增删该查
     控制器类和前端的操作关系能理解码？
	@RequestMapping("/devicetype") 前端的url参数设置
	@RequestMapping(value="/", method=RequestMethod.GET)
	前端的url参数设置
	/devicetype/？
	
2增加一个调试工具
   restclient的使用？
   
20200508
现在到目前为止，主要是做个javaweb的后端学习，也是基础性的学习。
前后端分离。

知识巩固：
编码实现
  1@,创建数据库表格                                           DeviceType  (完成了)
  2@,创建数据库表格的增删改查Jpa接口      DeviceTypeRepository (完成了)
  3@,创建服务类                                                   DeviceTypeService (完成了)
  4@,创建前端数据接口                                       DeviceTypeController (完成了)
  5@,调试      
  		restclient工具调试get，put，post，delete；mysql数据操作工具
  		http://127.0.0.1:8083/node/   (完成了)                                       
  6@,优化
  7@,逻辑业务处理，if
  8@交付测试。
  9@前端页面的内容（这个是扩展内容，不属于本学期的指定教学内容；因为同学们学的比较好，我根据上课情况，适当安排）
  
物联网网关（gateway）：
物联网网关的开机关机；
物联网网关的信息参数配置；
物联网网关节点的增删改查；


操作步骤：
1 建工程和建立模板 （完成了）
2 需求分析及编码--网关类的描述
编码实现
  1@,创建数据库表格        			 Node                                  
  2@,创建数据库表格的增删改查Jpa接口       NodeRepository
  3@,创建服务类                                 		 NodeService                 
  4@,创建前端数据接口                       		 NodeController                
  5@,调试      restclient工具调试get，put，post，delete；mysql数据操作工具                                          
  6@,优化
  7@,逻辑业务处理，if
  8@交付测试。
  9@前端页面的内容（这个是扩展内容，不属于本学期的指定教学内容；因为同学们学的比较好，我根据上课情况，适当安排）



