import { PrismaClient, Role, ProjectStatus, Priority, TaskStatus } from '@prisma/client';
import bcrypt from 'bcryptjs';
const prisma = new PrismaClient();
async function main() {
  const passwordHash=await bcrypt.hash('DemoPass123!',12);
  const company=await prisma.company.upsert({where:{id:'demo-company'},update:{},create:{id:'demo-company',name:'Acme Digital',timezone:'Asia/Kolkata'}});
  const users=await Promise.all([['admin@protime.local','Aarav Admin',Role.ADMIN],['manager@protime.local','Meera Manager',Role.MANAGER],['employee@protime.local','Riya Employee',Role.EMPLOYEE]].map(([email,name,role])=>prisma.user.upsert({where:{companyId_email:{companyId:company.id,email:String(email)}},update:{},create:{companyId:company.id,email:String(email),name:String(name),role:role as Role,passwordHash}})));
  const project=await prisma.project.upsert({where:{companyId_name:{companyId:company.id,name:'E-Commerce Platform'}},update:{},create:{companyId:company.id,name:'E-Commerce Platform',client:'Northstar Retail',description:'Customer storefront refresh',status:ProjectStatus.ACTIVE,budget:500000}});
  for(const user of users) await prisma.projectMember.upsert({where:{projectId_userId:{projectId:project.id,userId:user.id}},update:{},create:{projectId:project.id,userId:user.id}});
  await prisma.task.upsert({where:{id:'demo-task-auth'},update:{},create:{id:'demo-task-auth',projectId:project.id,assigneeId:users[2].id,title:'Implement Authentication',status:TaskStatus.IN_PROGRESS,priority:Priority.HIGH}});
}
main().finally(()=>prisma.$disconnect());