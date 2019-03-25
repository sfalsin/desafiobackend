package br.com.picpay.restapi.repository;

import java.util.List;

import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import br.com.picpay.restapi.domain.ImportedUser;

@Repository
public interface ImportedUserRepository extends PagingAndSortingRepository<ImportedUser, String>  {
	
	List<ImportedUser> findByNameIgnoreCaseContainingOrderByPriority(@Param("name") String name);

}
